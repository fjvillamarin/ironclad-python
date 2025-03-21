# CreateAWebhook400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**param** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.create_a_webhook400_response import CreateAWebhook400Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAWebhook400Response from a JSON string
create_a_webhook400_response_instance = CreateAWebhook400Response.from_json(json)
# print the JSON string representation of the object
print(CreateAWebhook400Response.to_json())

# convert the object into a dict
create_a_webhook400_response_dict = create_a_webhook400_response_instance.to_dict()
# create an instance of CreateAWebhook400Response from a dict
create_a_webhook400_response_from_dict = CreateAWebhook400Response.from_dict(create_a_webhook400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


