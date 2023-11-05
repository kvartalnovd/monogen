#!/usr/bin/env bash

# Throws error - if it is.
#
# @example: exitIfError $? "Your error text".
# @example: exitIfError $1 "Your error text".
function exitIfError() {
  local exit_code=$1
  shift
  [[ $exit_code ]] &&
    ((exit_code != 0)) && {
      echo "ERROR. $*" >&2;
      exit "$exit_code";
    }
}


# Loads environment's arguments from dotenv (.env) files
#
# @example: loadDotenvArgs ".env.dev"
function loadDotenvArgs() {
    if [ ! -f "${ENVIRONMENT_FILE}" ]; then
      exitIfError 0 "The environment file ${ENVIRONMENT_FILE} was not found in $(pwd)";
    fi
    # shellcheck disable=SC2005
    echo "$(cat $1 | grep -v '#' | sed 's/\r$//' | awk '/=/ {print $1}')";
}


SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null && pwd )";

# Changes the folder to: repository: /src/docker | Docker: /usr/src/app/docker
cd "$(dirname "${SCRIPT_DIR}")" || exit;

ENVIRONMENT_FILE=".env";
if [ ! -f ${ENVIRONMENT_FILE} ]; then
  # Check: If there is no production environment file, then we get a development environment file
  ENVIRONMENT_FILE=".env.dev";
fi


# Pulling out environment variables
# shellcheck disable=SC2046
export $(loadDotenvArgs "${ENVIRONMENT_FILE}");

DOCKER_FILE="docker-compose.yml";
COMPOSE="docker-compose -f ${DOCKER_FILE}";
