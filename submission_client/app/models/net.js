import DS from 'ember-data';

export default DS.Model.extend({

    name: DS.attr('string'),
    description: DS.attr('string'),
    group: DS.belongsTo("group"),
    resolver: DS.belongsTo('operation'),
    cases: DS.hasMany("case")

});

