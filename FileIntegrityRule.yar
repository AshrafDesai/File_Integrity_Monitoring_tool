import "hash"

rule FileIntegrityRule
{
    meta:
        description = "Detect changes in file content based on MD5 hash"
    strings:
        $expected_hash = "59a4dafe39e868e8b5ba9bbf373138a0" // Replace with the MD5 hash of the original file content
    condition:
        hash.md5(0, filesize) == $expected_hash
}
