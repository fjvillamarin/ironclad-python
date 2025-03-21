# CreateAWebhookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[WebhookEventTypeValue]**](WebhookEventTypeValue.md) | The event type(s) to trigger the webhook. Note: you can use &#x60;*&#x60; to receive events for all events, although we don&#39;t recommend this path, especially for environments with higher volume. | 
**target_url** | **str** | The URL to send the webhook event payload to. | 

## Example

```python
from openapi_client.models.create_a_webhook_request import CreateAWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAWebhookRequest from a JSON string
create_a_webhook_request_instance = CreateAWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAWebhookRequest.to_json())

# convert the object into a dict
create_a_webhook_request_dict = create_a_webhook_request_instance.to_dict()
# create an instance of CreateAWebhookRequest from a dict
create_a_webhook_request_from_dict = CreateAWebhookRequest.from_dict(create_a_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


