const express = require("express");
const router = express.Router();

const fs = require('fs');

const logic = require("../../ethereum/logic");

router.get("/", async (req,res,next) => {
    let message = await logic.getMessage();
    res.send(message);
})


router.post("/", async (req, res, next) => {
    try {
        let message = await logic.setMessage(req.body.message);

        // Writing message to a text file
        const filePath = '/home/arcturus/pvc/message.txt';

        fs.writeFile(filePath, message.transactionHash, 'utf8', (err) => {
            if (err) {
                console.error(err);
                res.status(500).send('Error writing to file');
            } else {
                console.log(`Message written to ${filePath}`);
                res.send(message.transactionHash);
            }
        });
    } catch (error) {
        console.error(error);
        res.status(500).send('Error processing the message');
    }
});



module.exports = router;