let big = '1'.repeat(53); console.log(String(parseInt(big, 2)) === String(0b1.concat('1'.repeat(52))) ? 'same' : 'diff');
