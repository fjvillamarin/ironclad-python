# CreateAWebhook200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**events** | **List[str]** |  | [optional] 
**target_url** | **str** |  | [optional] 
**company** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.create_a_webhook200_response import CreateAWebhook200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAWebhook200Response from a JSON string
create_a_webhook200_response_instance = CreateAWebhook200Response.from_json(json)
# print the JSON string representation of the object
print(CreateAWebhook200Response.to_json())

# convert the object into a dict
create_a_webhook200_response_dict = create_a_webhook200_response_instance.to_dict()
# create an instance of CreateAWebhook200Response from a dict
create_a_webhook200_response_from_dict = CreateAWebhook200Response.from_dict(create_a_webhook200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


