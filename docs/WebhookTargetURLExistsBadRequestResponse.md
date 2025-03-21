# WebhookTargetURLExistsBadRequestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**param** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.webhook_target_url_exists_bad_request_response import WebhookTargetURLExistsBadRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookTargetURLExistsBadRequestResponse from a JSON string
webhook_target_url_exists_bad_request_response_instance = WebhookTargetURLExistsBadRequestResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookTargetURLExistsBadRequestResponse.to_json())

# convert the object into a dict
webhook_target_url_exists_bad_request_response_dict = webhook_target_url_exists_bad_request_response_instance.to_dict()
# create an instance of WebhookTargetURLExistsBadRequestResponse from a dict
webhook_target_url_exists_bad_request_response_from_dict = WebhookTargetURLExistsBadRequestResponse.from_dict(webhook_target_url_exists_bad_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


