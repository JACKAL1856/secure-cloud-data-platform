resource "aws_iam_policy" "s3_read_only" {
  name        = "s3-read-only-policy"
  description = "Least privilege read-only access to a specific S3 bucket"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "s3:GetObject",
          "s3:ListBucket"
        ]
        Resource = [
          "arn:aws:s3:::secure-cloud-data-platform-demo",
          "arn:aws:s3:::secure-cloud-data-platform-demo/*"
        ]
      }
    ]
  })
}

resource "aws_iam_role" "app_role" {
  name = "secure-app-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "attach_policy" {
  role       = aws_iam_role.app_role.name
  policy_arn = aws_iam_policy.s3_read_only.arn
}


