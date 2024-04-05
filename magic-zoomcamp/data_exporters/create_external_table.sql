-- Docs: https://docs.mage.ai/guides/sql-blocks
--Create an external table using the Green Taxi Trip Records Data for 2022.
CREATE OR REPLACE EXTERNAL TABLE `zoomcamp-2024-psergios.ny_taxi.external_green_tripdata`
OPTIONS (
  format = 'parquet',
  uris = ['gs://zoomcamp_psergios/ny_taxi_data.parquet']
);
