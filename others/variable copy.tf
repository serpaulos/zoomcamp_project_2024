variable "credentials" {
  description = "My Credentials"
  default     = "../keys/google_creds.json"
}

variable "project" {
  description = "Project Name"
  default     = "de-zoomcamp-2024-411615"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "region" {
  description = "Project Region"
  default     = "us-central1"
}

variable "bg_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "zoom_project_retail"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "de-zoomcamp-2024-project"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}
