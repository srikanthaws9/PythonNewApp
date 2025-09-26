resource "aws_s3_bucket" "my_bucket" {
    bucket = "my-unikkue-bucket-name-12345"    
    
    tags = {
        Name        = "My bucket"
        Environment = "Dev"
        Team        = "DevOps"
    }
    }