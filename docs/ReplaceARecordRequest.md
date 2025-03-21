# ReplaceARecordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of record to be created. You can view available record types by retrieving records metadata. | 
**name** | **str** | The name of the record. | 
**properties** | [**CreateARecordRequestProperties**](CreateARecordRequestProperties.md) |  | 
**parent** | [**CreateARecordRequestParent**](CreateARecordRequestParent.md) |  | [optional] 
**children** | [**List[RecordPropertyLinkModel]**](RecordPropertyLinkModel.md) | List of objects containing the Record IDs or Ironclad IDs of the records to be set as child records of the current record. | [optional] 

## Example

```python
from openapi_client.models.replace_a_record_request import ReplaceARecordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceARecordRequest from a JSON string
replace_a_record_request_instance = ReplaceARecordRequest.from_json(json)
# print the JSON string representation of the object
print(ReplaceARecordRequest.to_json())

# convert the object into a dict
replace_a_record_request_dict = replace_a_record_request_instance.to_dict()
# create an instance of ReplaceARecordRequest from a dict
replace_a_record_request_from_dict = ReplaceARecordRequest.from_dict(replace_a_record_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


