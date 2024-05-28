#!/usr/bin/node

const request = require('request');

async function fetchCharacterNames(filmNum) {
    const filmURL = `https://swapi-api.hbtn.io/api/films/${filmNum}/`;

    try {
        const filmInfo = await new Promise((resolve, reject) => {
            request(filmURL, (err, res, body) => {
                if (err) {
                    reject(err);
                } else {
                    resolve(JSON.parse(body));
                }
            });
        });

        const charURLList = filmInfo.characters;

        for (const charURL of charURLList) {
            await new Promise((resolve, reject) => {
                request(charURL, (err, res, body) => {
                    if (err) {
                        console.error(err);
                    } else {
                        const characterInfo = JSON.parse(body);
                        console.log(characterInfo.name);
                    }
                    resolve();
                });
            });
        }
    } catch (error) {
        console.error(error);
    }
}

const filmNumber = process.argv[2];
fetchCharacterNames(filmNumber);

