
import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.toString()}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print);
};

const displaySchoolValue = async (schoolName) => {
  const getAsync = promisify(client.get).bind(client);
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(`Error retrieving value for ${schoolName}:`, err);
  }
};

const main = async () => {
	displaySchoolValue('ALX');
	setNewSchool('ALXSanFrancisco', '100');
	displaySchoolValue('ALXSanFrancisco');
};

main();
