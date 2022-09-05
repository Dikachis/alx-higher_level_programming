#!/usr/bin/node
'use strict';
if (process.argv[2] === undefined) {
    console.log('No argument');
} else {
    if (process.argv[2]) {
        console.log('Argument found');
    }
}
