load("@problem//:requirements.bzl", "requirement")

py_binary(
  name="sync_google_sheet",
  srcs = ["sync_google_sheet.py"],
  deps = [
    requirement("google-api-core"),
    requirement("google-auth-oauthlib"),
    requirement("google-api-python-client")
  ]
)