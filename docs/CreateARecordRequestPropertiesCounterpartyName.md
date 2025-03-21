# CreateARecordRequestPropertiesCounterpartyName

The name of the counterparty.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'string']
**value** | **str** | The name of the counterparty. | [optional] 

## Example

```python
from openapi_client.models.create_a_record_request_properties_counterparty_name import CreateARecordRequestPropertiesCounterpartyName

# TODO update the JSON string below
json = "{}"
# create an instance of CreateARecordRequestPropertiesCounterpartyName from a JSON string
create_a_record_request_properties_counterparty_name_instance = CreateARecordRequestPropertiesCounterpartyName.from_json(json)
# print the JSON string representation of the object
print(CreateARecordRequestPropertiesCounterpartyName.to_json())

# convert the object into a dict
create_a_record_request_properties_counterparty_name_dict = create_a_record_request_properties_counterparty_name_instance.to_dict()
# create an instance of CreateARecordRequestPropertiesCounterpartyName from a dict
create_a_record_request_properties_counterparty_name_from_dict = CreateARecordRequestPropertiesCounterpartyName.from_dict(create_a_record_request_properties_counterparty_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


