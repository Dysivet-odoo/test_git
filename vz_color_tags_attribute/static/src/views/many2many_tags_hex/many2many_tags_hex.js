import { _t } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";
import { TagsList } from "@web/core/tags_list/tags_list";

import {
    Many2ManyTagsFieldColorEditable,
    many2ManyTagsFieldColorEditable,
} from "@web/views/fields/many2many_tags/many2many_tags_field";

function normalizeHexColor(value) {
    if (!value) {
        return null;
    }
    const v = String(value).trim();
    const m = /^#([0-9a-fA-F]{6})$/.exec(v);
    if (!m) {
        return null;
    }
    return `#${m[1].toUpperCase()}`;
}

function getReadableTextColor(hex) {
    const v = normalizeHexColor(hex);
    if (!v) {
        return null;
    }
    const r = parseInt(v.slice(1, 3), 16);
    const g = parseInt(v.slice(3, 5), 16);
    const b = parseInt(v.slice(5, 7), 16);
    const yiq = (r * 299 + g * 587 + b * 114) / 1000;
    return yiq >= 160 ? "#111827" : "#FFFFFF";
}

export class VzTagsListHex extends TagsList {
    static template = "vz_color_tags_attribute.TagsListHex";
}

export class TestTag extends TagsList{
    static test = "vz_color_tags_attribute.TaglistHex";
    getTest(){
        return 4;
    }
}

export class Many2ManyTagsHexField extends Many2ManyTagsFieldColorEditable {
    static template = Many2ManyTagsFieldColorEditable.template;
    static components = {
        ...Many2ManyTagsFieldColorEditable.components,
        TagsList: VzTagsListHex,
    };

    static props = {
        ...Many2ManyTagsFieldColorEditable.props,
        hexColorField: { type: String, optional: true },
    };

    static defaultProps = {
        ...Many2ManyTagsFieldColorEditable.defaultProps,
    };

    getTagProps(record) {
        const props = super.getTagProps(record);
        const hexField = this.props.hexColorField;
        const hex = hexField ? normalizeHexColor(record.data[hexField]) : null;
        props.colorHex = hex;
        props.textColor = getReadableTextColor(hex);
        // If no colorField is configured, default to 0 (used by some templates/classes).
        props.colorIndex = this.props.colorField ? record.data[this.props.colorField] : 0;
        return props;
    }
}

export class KanbanMany2ManyTagsHexField extends Many2ManyTagsHexField {
    static template = "vz_color_tags_attribute.KanbanMany2ManyTagsHexField";

    get tags() {
        const tags = super.tags;
        // In standard many2many_tags kanban, tags with colorIndex == 0 are considered hidden.
        // For hex-only usage (no color_field provided), keep all tags.
        if (!this.props.colorField) {
            return tags;
        }
        return tags.reduce((kanbanTags, tag) => {
            if (tag.colorIndex !== 0) {
                delete tag.onClick;
                kanbanTags.push(tag);
            }
            return kanbanTags;
        }, []);
    }
}

export const many2ManyTagsHexField = {
    ...many2ManyTagsFieldColorEditable,
    component: Many2ManyTagsHexField,
    displayName: _t("Tags (Hex)"),
    supportedOptions: [
        ...many2ManyTagsFieldColorEditable.supportedOptions,
        {
            label: _t("Hex color field"),
            name: "hex_color_field",
            type: "field",
            availableTypes: ["char"],
        },
    ],
    relatedFields: ({ options }) => {
        const relatedFields = many2ManyTagsFieldColorEditable.relatedFields({ options });
        if (options.hex_color_field) {
            relatedFields.push({ name: options.hex_color_field, type: "char", readonly: false });
        }
        return relatedFields;
    },
    extractProps(fieldInfo, dynamicInfo) {
        const props = many2ManyTagsFieldColorEditable.extractProps(...arguments);
        props.hexColorField = fieldInfo.options.hex_color_field;
        return props;
    },
};

export const kanbanMany2ManyTagsHexField = {
    ...many2ManyTagsHexField,
    component: KanbanMany2ManyTagsHexField,
};

registry.category("fields").add("many2many_tags_hex", many2ManyTagsHexField);
registry.category("fields").add("form.many2many_tags_hex", many2ManyTagsHexField);
registry.category("fields").add("kanban.many2many_tags_hex", kanbanMany2ManyTagsHexField);
