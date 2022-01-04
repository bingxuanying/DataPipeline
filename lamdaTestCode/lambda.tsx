import { Context, APIGatewayEvent } from 'aws-lambda';
import { createConnection, Connection } from 'promise-mysql';

interface Response {
    statusCode: number;
    body: string;
}

const getClient = async (): Promise<Connection> => {
    const { username, password, host, port, dbClusterIdentifier } = JSON.parse(SECRECT);
    const conn = await createConnection({
        host: host,
        multipleStatements: false,
        user: username,
        password: password,
        database: dbClusterIdentifier,
        port: parseInt(port)
    });

    return conn;
};

export const randomGet = async (_event: APIGatewayEvent, _context: Context): Promise<Response> => {
    //life check.
    return {
        body: 'hello world',
        statusCode: 200
    };
};

export const randomPost = async (event: APIGatewayEvent, _context: Context): Promise<Response> => {

    const parsed = event.body ? JSON.parse(event.body) : null;
    const { table, keys, values } = parsed;
    const query = `INSERT INTO ${table} (${keys}) VALUES ${values}; `;

    const conn = await getClient();
    await conn.query(query);
    conn.destroy();

    //life check.
    return {
        body: 'successfully insert',
        statusCode: 200
    };
};