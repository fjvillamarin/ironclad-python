# EmailResponseModel


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
**attachments** | [**List[OutboundAttachmentModel]**](OutboundAttachmentModel.md) |  | [optional] 
**recipients** | **List[str]** |  | [optional] 
**cc** | **List[str]** |  | [optional] 
**email_opened_timestamps** | [**List[OutboundEmailResponseEmailOpenedTimestampsInner]**](OutboundEmailResponseEmailOpenedTimestampsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.email_response_model import EmailResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of EmailResponseModel from a JSON string
email_response_model_instance = EmailResponseModel.from_json(json)
# print the JSON string representation of the object
print(EmailResponseModel.to_json())

# convert the object into a dict
email_response_model_dict = email_response_model_instance.to_dict()
# create an instance of EmailResponseModel from a dict
email_response_model_from_dict = EmailResponseModel.from_dict(email_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


