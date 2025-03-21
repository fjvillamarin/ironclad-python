# UpdateAWebhookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | **List[str]** | The type of events that will trigger a notification to the target URL. | [optional] 
**target_url** | **str** | The URL of where the notification gets sent. | [optional] 

## Example

```python
from openapi_client.models.update_a_webhook_request import UpdateAWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAWebhookRequest from a JSON string
update_a_webhook_request_instance = UpdateAWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAWebhookRequest.to_json())

# convert the object into a dict
update_a_webhook_request_dict = update_a_webhook_request_instance.to_dict()
# create an instance of UpdateAWebhookRequest from a dict
update_a_webhook_request_from_dict = UpdateAWebhookRequest.from_dict(update_a_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


