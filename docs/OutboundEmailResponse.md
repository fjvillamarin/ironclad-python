# OutboundEmailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**author** | [**ActivityAuthorModel**](ActivityAuthorModel.md) |  | [optional] 
**timestamp** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**recipients** | **List[str]** |  | [optional] 
**cc** | **List[str]** |  | [optional] 
**attachments** | [**List[OutboundAttachmentModel]**](OutboundAttachmentModel.md) |  | [optional] 
**email_opened_timestamps** | [**List[OutboundEmailResponseEmailOpenedTimestampsInner]**](OutboundEmailResponseEmailOpenedTimestampsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.outbound_email_response import OutboundEmailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OutboundEmailResponse from a JSON string
outbound_email_response_instance = OutboundEmailResponse.from_json(json)
# print the JSON string representation of the object
print(OutboundEmailResponse.to_json())

# convert the object into a dict
outbound_email_response_dict = outbound_email_response_instance.to_dict()
# create an instance of OutboundEmailResponse from a dict
outbound_email_response_from_dict = OutboundEmailResponse.from_dict(outbound_email_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


