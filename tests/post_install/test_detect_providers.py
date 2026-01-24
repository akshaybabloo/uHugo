import os
import toml
import yaml
from uhugo.post_install.detect_providers import (
    check_hugo_file,
    check_providers_fs,
    Provider,
)


def test_check_hugo_file_toml(tmp_path):
    config_data = {
        "uhugo": {
            "name": "cloudflare",
            "project": "gollahalli-com",
            "api_key": "env:cloudflare_key",
            "account_id": "env:cloudflare_account_id",
            "email_address": "env:cloudflare_email",
        }
    }
    config_file = tmp_path / "config.toml"
    with open(config_file, "w") as f:
        toml.dump(config_data, f)

    assert check_hugo_file(cwd=tmp_path) == Provider(
        name="cloudflare",
        project="gollahalli-com",
        file_name=None,
        api_key="env:cloudflare_key",
        account_id="env:cloudflare_account_id",
        email_address="env:cloudflare_email",
        path=None,
    )


def test_check_hugo_file_yaml(tmp_path):
    config_data = {
        "uhugo": {
            "name": "cloudflare",
            "project": "gollahalli-com",
            "api_key": "env:cloudflare_key",
            "account_id": "env:cloudflare_account_id",
            "email_address": "env:cloudflare_email",
        }
    }
    config_file = tmp_path / "config.yaml"
    with open(config_file, "w") as f:
        yaml.dump(config_data, f)

    assert check_hugo_file(cwd=tmp_path) == Provider(
        name="cloudflare",
        project="gollahalli-com",
        file_name=None,
        api_key="env:cloudflare_key",
        account_id="env:cloudflare_account_id",
        email_address="env:cloudflare_email",
        path=None,
    )


def test_check_hugo_file_no_file(tmp_path):
    # Ensure no config files exist in tmp_path
    assert check_hugo_file(cwd=tmp_path) == Provider()


def test_check_providers_fs(tmp_path):
    # Create dummy provider files
    (tmp_path / "vercel.json").touch()
    (tmp_path / "netlify.toml").touch()

    expected = [
        Provider(
            name="vercel",
            path=str(tmp_path / "vercel.json"),
        ),
        Provider(
            name="netlify",
            path=str(tmp_path / "netlify.toml"),
        ),
    ]

    # Sort by name to ensure consistent order for comparison,
    # as the implementation iterates through a fixed list but order of append depends on file existence.
    # Actually, check_providers_fs iterates over a fixed list: ["netlify.yaml", "vercel.json", "netlify.toml", "wrangler.toml"]
    # So vercel comes before netlify.toml.

    result = check_providers_fs(cwd=tmp_path)
    assert len(result) == 2
    assert result[0].name == "vercel"
    assert result[1].name == "netlify"
