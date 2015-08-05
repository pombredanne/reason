#!/bin/bash

mvn clean compile package
mvn install dependency:copy-dependencies -Dtransitive=true
