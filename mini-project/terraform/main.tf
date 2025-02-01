resource "google_project" "project" {
  name       = "mini-project"
  project_id = "mini-project-${random_string.unique_suffix.result}"
  org_id     = var.org_id
  billing_account = var.billing_account_id
}

resource "random_string" "unique_suffix" {
  length  = 8
  upper   = false
  lower   = true
  number  = true
  special = false
}

resource "google_compute_network" "default" {
  name                    = "mini-project-network"
  auto_create_subnetworks = "true"
}

resource "google_app_engine_application" "app" {
  location_id = "us-central"
}

resource "google_cloud_run_service" "backend" {
  name     = "backend-service"
  location = "us-central1"

  template {
    spec {
      containers {
        image = "gcr.io/${google_project.project.project_id}/backend:latest"
      }
    }
  }
}

resource "google_cloud_run_service" "frontend" {
  name     = "frontend-service"
  location = "us-central1"

  template {
    spec {
      containers {
        image = "gcr.io/${google_project.project.project_id}/frontend:latest"
      }
    }
  }
}

output "project_id" {
  value = google_project.project.project_id
}

output "backend_url" {
  value = google_cloud_run_service.backend.status[0].url
}

output "frontend_url" {
  value = google_cloud_run_service.frontend.status[0].url
}