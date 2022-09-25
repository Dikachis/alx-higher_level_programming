#!/usr/bin/node
// assuming we have; arglist = node 2-argument.js 'This', 'is', 'my', 'terminal'
// assuming we have; arglist = ./2-argument.js 'This', 'is', 'my', 'terminal'
// count by number -->
// process.argv.length = argc = 6 (that is; argc1 = './' or 'node', argc2 = '2-argument.js', argc3 = 'This', argc4 = 'is', argc5 = 'my', argc6 = 'terminal')
//index var_count -->
// process.argv.length = argv[i] = 5 (that is; argv[0] = './' or 'node', argv[1] = '2-argument.js', argv[2] = 'This', argv[3] = 'is', argv[4] = 'my', argv[5] = 'terminal')
// therefore, process.argv begins with argc === 3 or argv[2]. That is, process.argv is argc === 3 or argv[2]
// if process.argv[2] is not available or none, it is said to be === undefined)

const argc = process.argv.length;
if (argc === 2) {
  console.log('No argument');
} else if (argc === 3) {
  console.log('Argument found');
} else if (argc > 3) {
  console.log('Arguments found');
}
