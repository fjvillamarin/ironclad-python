# OutboundAttachmentModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 
**download** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.outbound_attachment_model import OutboundAttachmentModel

# TODO update the JSON string below
json = "{}"
# create an instance of OutboundAttachmentModel from a JSON string
outbound_attachment_model_instance = OutboundAttachmentModel.from_json(json)
# print the JSON string representation of the object
print(OutboundAttachmentModel.to_json())

# convert the object into a dict
outbound_attachment_model_dict = outbound_attachment_model_instance.to_dict()
# create an instance of OutboundAttachmentModel from a dict
outbound_attachment_model_from_dict = OutboundAttachmentModel.from_dict(outbound_attachment_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


