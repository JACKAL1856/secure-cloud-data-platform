resource "aws_s3_bucket" "cloudtrail_logs" {
  bucket = "secure-cloud-data-platform-cloudtrail-logs"

  tags = {
    Name        = "cloudtrail-logs"
    Environment = "security-lab"
  }
}

resource "aws_s3_bucket_public_access_block" "cloudtrail_block_public" {
  bucket = aws_s3_bucket.cloudtrail_logs.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "cloudtrail_encryption" {
  bucket = aws_s3_bucket.cloudtrail_logs.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_cloudtrail" "main_trail" {
  name                          = "secure-cloudtrail"
  s3_bucket_name                = aws_s3_bucket.cloudtrail_logs.bucket
  include_global_service_events = true
  is_multi_region_trail         = true
  enable_logging                = true

  event_selector {
    read_write_type           = "All"
    include_management_events = true

    data_resource {
      type   = "AWS::S3::Object"
      values = ["arn:aws:s3:::secure-cloud-data-platform-demo/"]
    }
  }
}

