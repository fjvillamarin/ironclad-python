# RecordModelProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agreement_date** | [**RecordModelPropertiesAgreementDate**](RecordModelPropertiesAgreementDate.md) |  | [optional] 
**counterparty_name** | [**RecordModelPropertiesCounterpartyName**](RecordModelPropertiesCounterpartyName.md) |  | [optional] 
**counterparty_email** | [**RecordModelPropertiesCounterpartyEmail**](RecordModelPropertiesCounterpartyEmail.md) |  | [optional] 
**hourly_rate** | [**RecordModelPropertiesHourlyRate**](RecordModelPropertiesHourlyRate.md) |  | [optional] 

## Example

```python
from openapi_client.models.record_model_properties import RecordModelProperties

# TODO update the JSON string below
json = "{}"
# create an instance of RecordModelProperties from a JSON string
record_model_properties_instance = RecordModelProperties.from_json(json)
# print the JSON string representation of the object
print(RecordModelProperties.to_json())

# convert the object into a dict
record_model_properties_dict = record_model_properties_instance.to_dict()
# create an instance of RecordModelProperties from a dict
record_model_properties_from_dict = RecordModelProperties.from_dict(record_model_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


