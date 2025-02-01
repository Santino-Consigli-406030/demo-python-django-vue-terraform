output "frontend_ip" {
  value = google_compute_instance.frontend_instance.network_interface[0].access_config[0].nat_ip
}

output "backend_ip" {
  value = google_compute_instance.backend_instance.network_interface[0].access_config[0].nat_ip
}

output "frontend_url" {
  value = "http://${google_compute_instance.frontend_instance.network_interface[0].access_config[0].nat_ip}"
}

output "backend_url" {
  value = "http://${google_compute_instance.backend_instance.network_interface[0].access_config[0].nat_ip}:8000"
}