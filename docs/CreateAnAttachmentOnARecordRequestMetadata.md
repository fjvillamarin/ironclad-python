# CreateAnAttachmentOnARecordRequestMetadata

The `metadata` property's value must be `{\"filename\": \"[YOUR_FILE_NAME]\"}`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | The name of the file. Must have a supported file extension (.adoc, .asice, .bdoc, .csv, .ddoc, .doc, .docx, .edoc, .eml, .gif, .htm, .jpeg, .jpg, .msg, .pdf, .png, .ppt, .pptx, .rtf,.tif, .txt, .xls, .xlsx, .xml). | [optional] 

## Example

```python
from openapi_client.models.create_an_attachment_on_a_record_request_metadata import CreateAnAttachmentOnARecordRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAnAttachmentOnARecordRequestMetadata from a JSON string
create_an_attachment_on_a_record_request_metadata_instance = CreateAnAttachmentOnARecordRequestMetadata.from_json(json)
# print the JSON string representation of the object
print(CreateAnAttachmentOnARecordRequestMetadata.to_json())

# convert the object into a dict
create_an_attachment_on_a_record_request_metadata_dict = create_an_attachment_on_a_record_request_metadata_instance.to_dict()
# create an instance of CreateAnAttachmentOnARecordRequestMetadata from a dict
create_an_attachment_on_a_record_request_metadata_from_dict = CreateAnAttachmentOnARecordRequestMetadata.from_dict(create_an_attachment_on_a_record_request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


