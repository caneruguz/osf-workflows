import DS from 'ember-data';

export default DS.Model.extend({

    messageType: DS.attr('string'),
    timestamp: DS.attr('date'),
    origin: DS.hasMany('transition', {inverse: 'messages'}),
    response: DS.belongsTo('location', {inverse: "caller"}),
    caxe: DS.belongsTo('case', {inverse: "messages"}),
    content: DS.attr('string'),
    view: DS.attr(),
    section: DS.attr('string'),
    responseToken: DS.belongsTo('token', {inverse: 'requestMessage'})

});

