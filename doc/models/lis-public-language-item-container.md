
# LIS Public Language Item Container

## Structure

`LISPublicLanguageItemContainer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `language_items` | [`List of LISPublicLanguageItem`](../../doc/models/lis-public-language-item.md) | Optional | Gets or sets the language items. |
| `default_text` | `string` | Optional | Gets or sets the default text. |

## Example (as JSON)

```json
{
  "languageItems": [
    {
      "languageItemId": 191,
      "languageId": 5,
      "cultureName": "cultureName9",
      "languageName": "languageName5",
      "text": "text5"
    },
    {
      "languageItemId": 190,
      "languageId": 6,
      "cultureName": "cultureName8",
      "languageName": "languageName6",
      "text": "text4"
    },
    {
      "languageItemId": 189,
      "languageId": 7,
      "cultureName": "cultureName7",
      "languageName": "languageName7",
      "text": "text3"
    }
  ],
  "defaultText": "defaultText2"
}
```

