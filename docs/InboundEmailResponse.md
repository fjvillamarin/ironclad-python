# InboundEmailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email_thread_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**author** | [**ActivityAuthorModel**](ActivityAuthorModel.md) |  | [optional] 
**timestamp** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**attachments** | [**List[InboundAttachmentModel]**](InboundAttachmentModel.md) |  | [optional] 

## Example

```python
from openapi_client.models.inbound_email_response import InboundEmailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InboundEmailResponse from a JSON string
inbound_email_response_instance = InboundEmailResponse.from_json(json)
# print the JSON string representation of the object
print(InboundEmailResponse.to_json())

# convert the object into a dict
inbound_email_response_dict = inbound_email_response_instance.to_dict()
# create an instance of InboundEmailResponse from a dict
inbound_email_response_from_dict = InboundEmailResponse.from_dict(inbound_email_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


