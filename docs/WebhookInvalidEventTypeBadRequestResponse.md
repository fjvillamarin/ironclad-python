# WebhookInvalidEventTypeBadRequestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**param** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.webhook_invalid_event_type_bad_request_response import WebhookInvalidEventTypeBadRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookInvalidEventTypeBadRequestResponse from a JSON string
webhook_invalid_event_type_bad_request_response_instance = WebhookInvalidEventTypeBadRequestResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookInvalidEventTypeBadRequestResponse.to_json())

# convert the object into a dict
webhook_invalid_event_type_bad_request_response_dict = webhook_invalid_event_type_bad_request_response_instance.to_dict()
# create an instance of WebhookInvalidEventTypeBadRequestResponse from a dict
webhook_invalid_event_type_bad_request_response_from_dict = WebhookInvalidEventTypeBadRequestResponse.from_dict(webhook_invalid_event_type_bad_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


