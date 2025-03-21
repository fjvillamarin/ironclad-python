# RecordModelPropertiesHourlyRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**value** | [**RecordModelPropertiesHourlyRateValue**](RecordModelPropertiesHourlyRateValue.md) |  | [optional] 

## Example

```python
from openapi_client.models.record_model_properties_hourly_rate import RecordModelPropertiesHourlyRate

# TODO update the JSON string below
json = "{}"
# create an instance of RecordModelPropertiesHourlyRate from a JSON string
record_model_properties_hourly_rate_instance = RecordModelPropertiesHourlyRate.from_json(json)
# print the JSON string representation of the object
print(RecordModelPropertiesHourlyRate.to_json())

# convert the object into a dict
record_model_properties_hourly_rate_dict = record_model_properties_hourly_rate_instance.to_dict()
# create an instance of RecordModelPropertiesHourlyRate from a dict
record_model_properties_hourly_rate_from_dict = RecordModelPropertiesHourlyRate.from_dict(record_model_properties_hourly_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


