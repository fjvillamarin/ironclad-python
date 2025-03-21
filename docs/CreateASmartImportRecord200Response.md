# CreateASmartImportRecord200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_id** | **str** | Record ID of the new created record | [optional] 
**import_id** | **str** |  | [optional] 
**remaining_credits** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.create_a_smart_import_record200_response import CreateASmartImportRecord200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateASmartImportRecord200Response from a JSON string
create_a_smart_import_record200_response_instance = CreateASmartImportRecord200Response.from_json(json)
# print the JSON string representation of the object
print(CreateASmartImportRecord200Response.to_json())

# convert the object into a dict
create_a_smart_import_record200_response_dict = create_a_smart_import_record200_response_instance.to_dict()
# create an instance of CreateASmartImportRecord200Response from a dict
create_a_smart_import_record200_response_from_dict = CreateASmartImportRecord200Response.from_dict(create_a_smart_import_record200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


