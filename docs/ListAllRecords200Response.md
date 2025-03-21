# ListAllRecords200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] [default to 0]
**page_size** | **int** |  | [optional] [default to 0]
**count** | **int** |  | [optional] [default to 0]
**list** | [**List[RecordModel]**](RecordModel.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_all_records200_response import ListAllRecords200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllRecords200Response from a JSON string
list_all_records200_response_instance = ListAllRecords200Response.from_json(json)
# print the JSON string representation of the object
print(ListAllRecords200Response.to_json())

# convert the object into a dict
list_all_records200_response_dict = list_all_records200_response_instance.to_dict()
# create an instance of ListAllRecords200Response from a dict
list_all_records200_response_from_dict = ListAllRecords200Response.from_dict(list_all_records200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


