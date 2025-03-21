# ListAllWebhooks200ResponseListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**events** | **List[str]** |  | [optional] 
**target_url** | **str** |  | [optional] 
**company** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.list_all_webhooks200_response_list_inner import ListAllWebhooks200ResponseListInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllWebhooks200ResponseListInner from a JSON string
list_all_webhooks200_response_list_inner_instance = ListAllWebhooks200ResponseListInner.from_json(json)
# print the JSON string representation of the object
print(ListAllWebhooks200ResponseListInner.to_json())

# convert the object into a dict
list_all_webhooks200_response_list_inner_dict = list_all_webhooks200_response_list_inner_instance.to_dict()
# create an instance of ListAllWebhooks200ResponseListInner from a dict
list_all_webhooks200_response_list_inner_from_dict = ListAllWebhooks200ResponseListInner.from_dict(list_all_webhooks200_response_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


