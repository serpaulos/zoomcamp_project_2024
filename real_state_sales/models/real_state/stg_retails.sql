{{ config(
    materialized='view'
) }}

SELECT
    list_year,
    town,
    assessed_value,
    sale_amount,
    sales_ratio,
    property_type,
    residential_type
FROM {{ source('real_state', 'real_state_sales_data') }}
WHERE residential_type != 'NA'