export class ObservatoryWebsocketClient {
  url: string;

  constructor(url: string) {
    this.url = url;
  }

  connect(): string {
    return `Connecting to ${this.url}`;
  }
}
