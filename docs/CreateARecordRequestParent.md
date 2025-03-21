# CreateARecordRequestParent

Object containing Record IDs or Ironclad IDs to be set as the parent of the current record.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.create_a_record_request_parent import CreateARecordRequestParent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateARecordRequestParent from a JSON string
create_a_record_request_parent_instance = CreateARecordRequestParent.from_json(json)
# print the JSON string representation of the object
print(CreateARecordRequestParent.to_json())

# convert the object into a dict
create_a_record_request_parent_dict = create_a_record_request_parent_instance.to_dict()
# create an instance of CreateARecordRequestParent from a dict
create_a_record_request_parent_from_dict = CreateARecordRequestParent.from_dict(create_a_record_request_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


