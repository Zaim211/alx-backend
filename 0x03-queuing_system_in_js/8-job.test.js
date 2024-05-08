import createPushNotificationsJobs from './8-job';
import { createQueue } from 'kue';
import { describe, it, before, after, afterEach } from 'mocha';
import { expect } from 'chai';

const queue = createQueue();

describe('Test function createPushNotificationJobs', function() {
  before(function() {
    queue.testMode.enter();
  });

  afterEach(function () {
    queue.testMode.clear();
  });

  after(function() {
    queue.testMode.exit();
  });

  it('check if jobs is not an array', function() {
    expect((() => createPushNotificationsJobs('test', queue))).to.throw(Error, 'Jobs is not an array');
  });

  it('Test creation of jobs', function() {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1524 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 8542 to verify your account'
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);

    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);

    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.eql(jobs[1]);
  });
});
