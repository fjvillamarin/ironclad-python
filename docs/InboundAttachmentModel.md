# InboundAttachmentModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 
**download** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.inbound_attachment_model import InboundAttachmentModel

# TODO update the JSON string below
json = "{}"
# create an instance of InboundAttachmentModel from a JSON string
inbound_attachment_model_instance = InboundAttachmentModel.from_json(json)
# print the JSON string representation of the object
print(InboundAttachmentModel.to_json())

# convert the object into a dict
inbound_attachment_model_dict = inbound_attachment_model_instance.to_dict()
# create an instance of InboundAttachmentModel from a dict
inbound_attachment_model_from_dict = InboundAttachmentModel.from_dict(inbound_attachment_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


