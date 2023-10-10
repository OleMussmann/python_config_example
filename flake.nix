{
  description = "config example";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system: let
      name = "config_example";
      version = "0.0.1";
      pkgs = nixpkgs.legacyPackages.${system};
      py = pkgs.python311Packages;
      python_packages = with py; [
        py.pint
        py.tomli
      ];
      system_packages = with pkgs; [
      ];
    in {
      devShells.default = pkgs.mkShell rec {
        packages = system_packages ++ python_packages;
      };
      #defaultPackage = packages.config_example;
      packages.default = with py; buildPythonApplication {
        inherit name;
        inherit version;
        src = ./.;
        format = "pyproject";
        buildInputs = with py; [ setuptools ];
        propagatedBuildInputs = python_packages;
      };
      apps.default = {
        type = "app";
        program = ''${self.packages."${system}".default}/bin/config_example'';
      };
    });
}
