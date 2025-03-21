# AttachmentNotFound

attachmentId Not Found Request Error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**param** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.attachment_not_found import AttachmentNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentNotFound from a JSON string
attachment_not_found_instance = AttachmentNotFound.from_json(json)
# print the JSON string representation of the object
print(AttachmentNotFound.to_json())

# convert the object into a dict
attachment_not_found_dict = attachment_not_found_instance.to_dict()
# create an instance of AttachmentNotFound from a dict
attachment_not_found_from_dict = AttachmentNotFound.from_dict(attachment_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


