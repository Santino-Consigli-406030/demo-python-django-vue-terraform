variable "project_name" {
  description = "The name of the GCP project"
  type        = string
  default     = "mini-project"
}

variable "region" {
  description = "The region where resources will be created"
  type        = string
  default     = "us-central1"
}

variable "zone" {
  description = "The zone where resources will be created"
  type        = string
  default     = "us-central1-a"
}

variable "instance_type" {
  description = "The type of VM instance to create"
  type        = string
  default     = "n1-standard-1"
}

variable "db_instance_name" {
  description = "The name of the Cloud SQL database instance"
  type        = string
  default     = "mini-project-db"
}

variable "db_user" {
  description = "The username for the database"
  type        = string
  default     = "db_user"
}

variable "db_password" {
  description = "The password for the database"
  type        = string
  sensitive   = true
}

variable "db_name" {
  description = "The name of the database"
  type        = string
  default     = "mini_project_db"
}