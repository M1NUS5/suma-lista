target "default" {
  dockerfile = "Dockerfile"
}

target "validate-build" {
  inherits = ["default"]
  call = "check"
}