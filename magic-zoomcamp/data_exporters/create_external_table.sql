-- Docs: https://docs.mage.ai/guides/sql-blocks
--Create an external table using the Green Taxi Trip Records Data for 2022.
CREATE OR REPLACE EXTERNAL TABLE `zoomcamp-2024-psergios.retail_project_dataset.real_state_sales_data`
OPTIONS (
  format = 'parquet',
  uris = ['gs://de-zoomcamp-2024-project/real_state_sales.parquet']
);
