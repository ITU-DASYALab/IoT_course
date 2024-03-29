// Acknowledgement/source: https://github.com/kizniche/ttgo-tbeam-sensor-node-bme280

function Decoder(bytes, port) {
    // Decode an uplink message from a buffer
    // (array) of bytes to an object of fields.
    var decoded = {};

    // Humidity
    var rawHum = bytes[0] + bytes[1] * 256;
    decoded.humidity = Math.round(sflt162f(rawHum) * 100 * 100) / 100;
    // Pressure
    var rawCo2 = bytes[2] + bytes[3] * 256;
    decoded.co2 = Math.round(sflt162f(rawCo2) * 100 * 100) / 10
    // Temperature
    var rawTemp = bytes[4] + bytes[5] * 256;
    decoded.temperature = Math.round(sflt162f(rawTemp) * 100 * 100) / 100

    return decoded;
}

function sflt162f(rawSflt16) {
    // rawSflt16 is the 2-byte number decoded from wherever;
    // it's in range 0..0xFFFF
    // bit 15 is the sign bit
    // bits 14..11 are the exponent
    // bits 10..0 are the the mantissa. Unlike IEEE format,
    // 	the msb is transmitted; this means that numbers
    //	might not be normalized, but makes coding for
    //	underflow easier.
    // As with IEEE format, negative zero is possible, so
    // we special-case that in hopes that JavaScript will
    // also cooperate.
    //
    // The result is a number in the open interval (-1.0, 1.0);
    //

    // throw away high bits for repeatability.
    rawSflt16 &= 0xFFFF;

    // special case minus zero:
    if (rawSflt16 === 0x8000)
        return -0.0;

    // extract the sign.
    var sSign = ((rawSflt16 & 0x8000) !== 0) ? -1 : 1;

    // extract the exponent
    var exp1 = (rawSflt16 >> 11) & 0xF;

    // extract the "mantissa" (the fractional part)
    var mant1 = (rawSflt16 & 0x7FF) / 2048.0;

    // convert back to a floating point number. We hope
    // that Math.pow(2, k) is handled efficiently by
    // the JS interpreter! If this is time critical code,
    // you can replace by a suitable shift and divide.
    return sSign * mant1 * Math.pow(2, exp1 - 15);
}