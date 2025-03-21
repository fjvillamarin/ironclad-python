# ListAllWebhooks200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] [default to 0]
**page_size** | **int** |  | [optional] [default to 0]
**list** | [**List[ListAllWebhooks200ResponseListInner]**](ListAllWebhooks200ResponseListInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_all_webhooks200_response import ListAllWebhooks200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllWebhooks200Response from a JSON string
list_all_webhooks200_response_instance = ListAllWebhooks200Response.from_json(json)
# print the JSON string representation of the object
print(ListAllWebhooks200Response.to_json())

# convert the object into a dict
list_all_webhooks200_response_dict = list_all_webhooks200_response_instance.to_dict()
# create an instance of ListAllWebhooks200Response from a dict
list_all_webhooks200_response_from_dict = ListAllWebhooks200Response.from_dict(list_all_webhooks200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


